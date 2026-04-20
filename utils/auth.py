class Auth:
    def __init__(self, repo: UserRepo):
        self._repo = repo

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(f"{password}".encode()).hexdigest()

    def verify_password(self, password: str, hashed: str) -> bool:
        salt, digest = hashed.split(":", 1)
        return hmac.compare_digest(digest, hashlib.sha256(f"{salt}{password}".encode()).hexdigest())

    def generate_token(self, username: str) -> str:
        validate_username(username)
        payload = f"{username}:{int(time.time() + 3600)}"
        sig = hmac.new(
            self._repo._SECRET.encode(),
            payload.encode(),
            hashlib.sha256,
        ).hexdigest()
        return f"{payload}:{sig}"

    def verify_token(self, token: str) -> str | None:
        try:
            username, expires, sig = token.rsplit(":", 2)
            if int(expires) < time.time():
                return None
            expected = hmac.new(
                self._repo._SECRET.encode(),
                f"{username}:{expires}".encode(),
                hashlib.sha256,
            ).hexdigest()
            if not hmac.compare_digest(sig, expected):
                return None
            user = self._repo.get_by_username(username)
            return username if (user and user.is_active) else None
        except Exception:
            return None

    def __getattr__(self, name):
        return getattr(self._repo, name)