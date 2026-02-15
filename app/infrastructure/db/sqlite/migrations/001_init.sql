CREATE TABLE IF NOT EXISTS users (
    vk_id INTEGER PRIMARY KEY,
    nickname TEXT NOT NULL,
    faction TEXT,
    position TEXT,
    rp_name TEXT,
    registered INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_levels (
    vk_id INTEGER NOT NULL,
    faction TEXT NOT NULL,
    level INTEGER NOT NULL,
    PRIMARY KEY (vk_id, faction),
    FOREIGN KEY (vk_id) REFERENCES users(vk_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pending_approvals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vk_id INTEGER NOT NULL,
    nickname TEXT NOT NULL,
    faction TEXT NOT NULL,
    desired_position TEXT,
    rp_name TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS invite_codes (
    code TEXT PRIMARY KEY,
    target_vk_id INTEGER,
    faction TEXT NOT NULL,
    level INTEGER NOT NULL,
    position TEXT,
    rp_name TEXT,
    is_leader INTEGER NOT NULL DEFAULT 0,
    used INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS action_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    actor_vk_id INTEGER,
    action TEXT NOT NULL,
    payload TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
