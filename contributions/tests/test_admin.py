from django.urls import reverse

from contributions.models import Contribution, Topic


class TestTopicAdmin:

    def test_changelist(self, admin_client):
        url = reverse("admin:contributions_topic_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:contributions_topic_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_add(self, admin_client, theme):
        url = reverse("admin:contributions_topic_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "label": "test_label",
                "theme": theme.pk,
                "description": "test_description"
            },
        )
        assert response.status_code == 302
        assert Topic.objects.filter(label="test_label").exists()

    def test_view_topic(self, admin_client, topic):
        topic = Topic.objects.get(label='test_label')
        url = reverse("admin:contributions_topic_change", kwargs={"object_id": topic.pk})
        response = admin_client.get(url)
        assert response.status_code == 200


class TestContributionAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:contributions_contribution_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:contributions_contribution_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_add(self, admin_client, theme, contributor):
        url = reverse("admin:contributions_contribution_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "resume": "test_resume",
                "theme": theme.pk,
                "contributor": contributor.pk,
                "url": "test_url"
            },
        )
        assert response.status_code == 302
        assert Contribution.objects.filter(resume="test_resume").exists()

    def test_view_contribution(self, admin_client, contribution):
        contribution = Contribution.objects.get(resume='test_resume')
        url = reverse("admin:contributions_contribution_change", kwargs={"object_id": contribution.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
