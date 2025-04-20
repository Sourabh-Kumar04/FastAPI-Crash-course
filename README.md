# 🧃 FastAPI ItemList CRUD API

This is a simple **FastAPI** project that provides basic **CRUD** (Create, Read, Update, Delete) operations for managing a list of items. Each item contains an `id`, `name`, and `origin`.

## 🚀 Features

- ✅ `GET /` — Basic welcome route.
- 📋 `GET /itemList` — Retrieve the list of all items.
- ➕ `POST /itemList` — Add a new item.
- 🔄 `PUT /itemList/{item_id}` — Update an existing item.
- ❌ `DELETE /itemList/{item_id}` — Delete an item.

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- Python 3.12+

## 📄 API Endpoints

### `GET /`
Returns a friendly welcome message.

```json
{
  "message": "Hello World"
}
```

---

### `GET /itemList`
Fetch the list of all stored items.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mango",
    "origin": "India"
  }
]
```

---

### `POST /itemList`
Add a new item to the list.

**Request Body:**
```json
{
  "id": 2,
  "name": "Banana",
  "origin": "Ecuador"
}
```

**Response:**
```json
{
  "message": "Item added successfully: ",
  "item": {
    "id": 2,
    "name": "Banana",
    "origin": "Ecuador"
  }
}
```

---

### `PUT /itemList/{item_id}`
Update an existing item based on its `id`.

**Request Body:**
```json
{
  "id": 2,
  "name": "Banana",
  "origin": "Philippines"
}
```

**Response:**
```json
{
  "messaege": "Item updated successfully",
  "item": {
    "id": 2,
    "name": "Banana",
    "origin": "Philippines"
  }
}
```

---

### `DELETE /itemList/{item_id}`
Delete an item by its `id`.

**Response:**
```json
{
  "messaege": "Item deleted successfully",
  "item": {
    "id": 2,
    "name": "Banana",
    "origin": "Philippines"
  }
}
```

---

## ⚠️ Notes

- The data is **stored in memory**, meaning any data added will be lost once the server restarts.
- This app is meant for learning/demo purposes only.

## 🛠️ How to Run

1. Create a virtual environment and install dependencies:

```bash
pip install fastapi uvicorn
```

2. Run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

3. Open your browser and visit:
- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Root Endpoint: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✨ Author

Made with ❤️ by [Sourabh Kumar](https://github.com/Sourabh-Kumar04)

---

