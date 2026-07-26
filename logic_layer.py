class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add(self, text, priority):
        text = text.strip()
        if not text:
            return
        existing_texts = [t["text"].lower() for t in self.tasks]
        if text.lower() in existing_texts:
            return
        task = {"text": text, "done": False, "priority": priority}
        self.tasks.append(task)
        self.storage.save(self.tasks)
        return task

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.storage.save(self.tasks)
            return task
        return None

    def toggle_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.storage.save(self.tasks)
            return self.tasks[index]
        return None

    def edit(self, index, new_text):
        new_text = new_text.strip()
        if not new_text:
            return
        if 0 <= index < len(self.tasks):
            self.tasks[index]["text"] = new_text
            self.storage.save(self.tasks)
            return self.tasks[index]
        return None

    def clear_done(self):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t["done"]]
        self.storage.save(self.tasks)
        return before - len(self.tasks)

    def clear_all(self):
        self.tasks.clear()
        self.storage.save(self.tasks)

    def search(self, query):
        query = query.strip().lower()
        if not query:
            return self.tasks

        result = []
        for t in self.tasks:
            if query in t["text"].lower():
                result.append(t)

        return result

    def stats(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        pending = total - done
        percent = int((done / total) * 100)

        return {"total": total, "done": done, "pending": pending, "percent": percent}
