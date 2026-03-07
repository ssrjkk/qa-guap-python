import pytest

class TestTeachers:

    def test_get_teachers_returns_200(self, session, base_url):
        response = session.get(f"{base_url}/users")
        assert response.status_code == 200

    def test_teachers_list_is_not_empty(self, session, base_url):
        response = session.get(f"{base_url}/users")
        teachers = response.json()
        assert len(teachers) > 0

    def test_teacher_has_name_and_email(self, session, base_url):
        response = session.get(f"{base_url}/users")
        teachers = response.json()
        for teacher in teachers:
            assert "name" in teacher, f"Нет имени у пользователя {teacher.get('id')}"
            assert "email" in teacher, f"Нет email у пользователя {teacher.get('id')}"

    def test_get_teacher_by_id(self, session, base_url):
        response = session.get(f"{base_url}/users/1")
        assert response.status_code == 200
        teacher = response.json()
        assert teacher["id"] == 1

    def test_get_nonexistent_teacher_returns_404(self, session, base_url):
        response = session.get(f"{base_url}/users/99999")
        assert response.status_code == 404

    def test_teacher_email_is_valid_format(self, session, base_url):
        response = session.get(f"{base_url}/users")
        teachers = response.json()
        for teacher in teachers:
            assert "@" in teacher["email"], \
                f"Некорректный email у преподавателя id={teacher['id']}: {teacher['email']}"

class TestSchedule:

    def test_get_all_lessons_returns_200(self, session, base_url):
        response = session.get(f"{base_url}/posts")
        assert response.status_code == 200

    def test_lessons_list_is_not_empty(self, session, base_url):
        response = session.get(f"{base_url}/posts")
        lessons = response.json()
        assert len(lessons) > 0

    def test_lesson_has_required_fields(self, session, base_url):
        response = session.get(f"{base_url}/posts")
        lessons = response.json()
        for lesson in lessons[:10]:
            assert "id" in lesson
            assert "userId" in lesson
            assert "title" in lesson
            assert "body" in lesson

    def test_get_lesson_by_id(self, session, base_url):
        response = session.get(f"{base_url}/posts/1")
        assert response.status_code == 200

    def test_get_nonexistent_lesson_returns_404(self, session, base_url):
        response = session.get(f"{base_url}/posts/99999")
        assert response.status_code == 404

    def test_filter_lessons_by_teacher(self, session, base_url):
        teacher_id = 1
        response = session.get(f"{base_url}/posts", params={"userId": teacher_id})
        lessons = response.json()
        assert len(lessons) > 0
        for lesson in lessons:
            assert lesson["userId"] == teacher_id

    def test_filter_by_nonexistent_teacher_returns_empty(self, session, base_url):
        response = session.get(f"{base_url}/posts", params={"userId": 99999})
        lessons = response.json()
        assert lessons == []

    @pytest.mark.parametrize("lesson_id", [1, 10, 25, 50, 100])
    def test_various_lesson_ids_return_200(self, session, base_url, lesson_id):
        response = session.get(f"{base_url}/posts/{lesson_id}")
        assert response.status_code == 200

class TestHomework:

    def test_get_all_homework_returns_200(self, session, base_url):
        response = session.get(f"{base_url}/todos")
        assert response.status_code == 200

    def test_homework_has_completed_field(self, session, base_url):
        response = session.get(f"{base_url}/todos")
        todos = response.json()
        for todo in todos[:10]:
            assert "completed" in todo
            assert isinstance(todo["completed"], bool)

    def test_add_new_homework(self, session, base_url):
        new_task = {
            "userId": 1,
            "title": "Подготовить отчёт по лабораторной работе №3",
            "completed": False
        }
        response = session.post(f"{base_url}/todos", json=new_task)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == new_task["title"]

    def test_mark_homework_as_done(self, session, base_url):
        response = session.patch(f"{base_url}/todos/1", json={"completed": True})
        assert response.status_code == 200
        data = response.json()
        assert data["completed"] is True
