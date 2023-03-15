from django.urls import reverse

from various.models import Theme


class TestThemeAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:various_theme_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:various_theme_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_add(self, admin_client):
        url = reverse("admin:various_theme_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "label": "test_label",
            },
        )
        assert response.status_code == 302
        assert Theme.objects.filter(label="test_label").exists()

    def test_view_topic(self, admin_client, theme):

        theme = Theme.objects.get(label='test_label')
        url = reverse("admin:various_theme_change", kwargs={"object_id": theme.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
