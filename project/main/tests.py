from .models import Todo, User
from .constants import StatusType

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class BaseTodoTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='password123')
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='password123')

        self.todo1 = Todo.objects.create(
            user=self.user1, title="User1 Todo", todo_status=StatusType.NOT_FINISHED)
        self.todo2 = Todo.objects.create(
            user=self.user2, title="User2 Todo", todo_status=StatusType.NOT_FINISHED)

        self.client = APIClient()


class CreateTodoTest(BaseTodoTest):
    def test_create_todo_authenticated(self):
        self.client.login(username='user1', password='password123')
        data = {
            'title': 'New Todo',
        }
        response = self.client.post(reverse('todo-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Todo')

    def test_create_todo_unauthenticated(self):
        data = {
            'title': 'New Todo',
        }
        response = self.client.post(reverse('todo-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class EditTodoTest(BaseTodoTest):
    def test_edit_own_todo(self):
        self.client.login(username='user1', password='password123')
        data = {'title': 'Updated Todo'}
        response = self.client.patch(reverse('todo-detail', args=[self.todo1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Todo')

    def test_edit_other_user_todo(self):
        self.client.login(username='user1', password='password123')
        data = {'title': 'Illegal Update'}
        response = self.client.patch(reverse('todo-detail', args=[self.todo2.id]), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GetTodosTest(BaseTodoTest):
    def test_get_own_todos(self):
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todos = Todo.objects.filter(user=self.user1)
        self.assertEqual(response.data["count"], todos.count())
        for result in response.data["results"]:
            self.assertEqual(result["title"], 'User1 Todo')

    def test_get_other_user_todo(self):
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('todo-detail', args=[self.todo2.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteTodoTest(BaseTodoTest):
    def test_delete_own_todo(self):
        self.client.login(username='user1', password='password123')
        response = self.client.delete(reverse('todo-detail', args=[self.todo1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_other_user_todo(self):
        self.client.login(username='user1', password='password123')
        response = self.client.delete(reverse('todo-detail', args=[self.todo2.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
