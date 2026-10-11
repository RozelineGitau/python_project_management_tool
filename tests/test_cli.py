import json

import main


def test_add_user(monkeypatch, tmp_path):
    data_file = tmp_path / "database.json"

    monkeypatch.setattr(main, "load_objects", lambda: ([], [], []))

    saved = {}

    def fake_save(users, projects, tasks):
        saved["users"] = users

    monkeypatch.setattr(main, "save_objects", fake_save)

    args = type(
        "Args",
        (),
        {"name": "Alex", "email": "alex@example.com"},
    )()

    main.add_user(args)

    assert len(saved["users"]) == 1
    assert saved["users"][0].name == "Alex"


def test_storage_round_trip(tmp_path):
    from utils.storage import save_data, load_data

    file_path = tmp_path / "database.json"

    data = {
        "users": [{"id": 1, "name": "Alex", "email": "alex@example.com"}],
        "projects": [],
        "tasks": [],
    }

    save_data(data, file_path)
    loaded = load_data(file_path)

    assert loaded == data
