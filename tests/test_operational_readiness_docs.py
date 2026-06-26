from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_operational_readiness_docs_exist() -> None:
    required_paths = [
        "docs/OPERATIONAL_READINESS_MATRIX.md",
        "docs/DRY_RUN_OPERATIONS_RUNBOOK.md",
        "docs/REVIEW_PACKET_TEMPLATE.md",
        "examples/dry-run/README.md",
        "examples/dry-run/DRY_RUN_001_OPERATION_REPORT.sample.md",
        "examples/dry-run/DRY_RUN_001_REVIEW_PACKET.sample.md",
    ]
    for path in required_paths:
        assert (ROOT / path).is_file(), path


def test_operational_readiness_matrix_preserves_inactive_state() -> None:
    text = read("docs/OPERATIONAL_READINESS_MATRIX.md")
    assert "DONATIONS_ACTIVE: NO" in text
    assert "WALLETS_PUBLISHED: NO" in text
    assert "ACTIVATION_APPROVED: NO" in text
    assert "GO_LIVE = NO" in text
    assert "FORBIDDEN" in text


def test_dry_run_runbook_preserves_go_no_go_result() -> None:
    text = read("docs/DRY_RUN_OPERATIONS_RUNBOOK.md")
    assert "GO_LIVE: NO" in text
    assert "production gates remain incomplete" in text
    assert "dry-run and external review only" in text
    assert "Stop the dry run if:" in text


def test_review_packet_template_tracks_evidence_and_blockers() -> None:
    text = read("docs/REVIEW_PACKET_TEMPLATE.md")
    for phrase in [
        "REPOSITORY_COMMIT:",
        "Review Packet Template",
        "unresolved blockers",
        "Latest CI run",
        "PASS_WITH_NOTES",
        "BLOCKED",
    ]:
        assert phrase in text


def test_sample_operation_report_remains_sample_only() -> None:
    text = read("examples/dry-run/DRY_RUN_001_OPERATION_REPORT.sample.md")
    assert "DRY-RUN-001" in text
    assert "DONATIONS_ACTIVE: NO" in text
    assert "WALLETS_PUBLISHED: NO" in text
    assert "ACTIVATION_APPROVED: NO" in text
    assert "GO_LIVE_DECISION: NO" in text
    assert "production gates remain incomplete" in text


def test_sample_review_packet_tracks_blockers_and_no_go_live() -> None:
    text = read("examples/dry-run/DRY_RUN_001_REVIEW_PACKET.sample.md")
    for phrase in [
        "DRY-RUN-001-REVIEW-PACKET",
        "SAMPLE_ONLY",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "GO_LIVE: NO",
        "DECISION: BLOCKED",
        "Production gates remain incomplete",
        "LIVE_RECEIVING_DETAILS_INCLUDED: NO",
        "REAL_BENEFICIARY_DATA_INCLUDED: NO",
        "GO_LIVE_APPROVED: NO",
    ]:
        assert phrase in text


def test_dry_run_evidence_loop_index_keeps_repeatable_order() -> None:
    text = read("examples/dry-run/README.md")
    for phrase in [
        "Dry-Run Evidence Loop",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "GO_LIVE: NO",
        "Read docs/DRY_RUN_OPERATIONS_RUNBOOK.md",
        "Review DRY_RUN_001_OPERATION_REPORT.sample.md",
        "Review DRY_RUN_001_REVIEW_PACKET.sample.md",
        "Compare blockers with docs/OPERATIONAL_READINESS_MATRIX.md",
        "IF any production gate remains incomplete:",
        "GO_LIVE = NO",
        "SAMPLE_ONLY",
    ]:
        assert phrase in text
