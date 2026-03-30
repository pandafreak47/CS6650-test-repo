# CS6650 Test Repo — Order Management Service

A small Python service used as a target codebase for the LLM cache coherence experiments. It models a simple order management system with four layers: **api → services → db → models**, plus a **utils** cross-cutting layer.

---

## File Dependency Graph

```
main.py
├── api/routes.py
│   ├── api/middleware.py
│   │   └── utils/auth.py
│   │       ├── db/user_repo.py
│   │       │   ├── db/connection.py          [leaf]
│   │       │   └── models/user.py            [leaf]
│   │       └── utils/validators.py           [leaf]
│   ├── services/user_service.py
│   │   ├── db/user_repo.py                   (see above)
│   │   ├── utils/validators.py               (see above)
│   │   └── utils/auth.py                     (see above)
│   ├── services/order_service.py
│   │   ├── db/order_repo.py
│   │   │   ├── db/connection.py              (see above)
│   │   │   └── models/order.py
│   │   │       └── models/user.py            (see above)
│   │   ├── services/user_service.py          (see above)
│   │   └── utils/validators.py               (see above)
│   └── services/email_service.py
│       └── utils/templates.py
│           └── models/order.py               (see above)
└── (logging, http.server — stdlib only)
```

Leaf nodes (no local imports):
- `models/user.py`
- `db/connection.py`
- `utils/validators.py`
- `utils/templates.py`

---

## Repository Structure

```
├── main.py                    # HTTP server entry point
├── api/
│   ├── routes.py              # Request handlers; wires services together
│   └── middleware.py          # @require_auth decorator; token verification
├── services/
│   ├── user_service.py        # User registration, lookup, deactivation
│   ├── order_service.py       # Order placement, cancellation, listing
│   └── email_service.py       # Transactional email (logs in dev)
├── db/
│   ├── connection.py          # SQLite connection + schema bootstrap
│   ├── user_repo.py           # CRUD for users table
│   └── order_repo.py          # CRUD for orders table
├── models/
│   ├── user.py                # User dataclass
│   └── order.py               # Order dataclass + OrderStatus enum
└── utils/
    ├── validators.py          # Email, username, order-item validation
    ├── templates.py           # Email body rendering
    └── auth.py                # Password hashing, HMAC token generation/verification
```

---

## Running

```bash
python main.py          # starts on port 8080 (override with PORT env var)
DB_PATH=test.db python main.py
```

### Example requests

```bash
# Register a user
curl -X POST localhost:8080/users/register \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"secret123"}'

# Place an order (requires Bearer token from generate_token())
curl -X POST localhost:8080/orders \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"items":["Widget A","Widget B"],"total":29.99}'

# Cancel an order
curl -X DELETE localhost:8080/orders/1 \
  -H "Authorization: Bearer <token>"
```
