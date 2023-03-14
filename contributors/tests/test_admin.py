from django.urls import reverse

from contributors.models import Contributor


class TestContributorAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:contributors_contributor_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:contributors_contributor_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_add(self, admin_client):
        url = reverse("admin:contributors_contributor_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "first_name": "test_firstname",
                "last_name": "test_last_name",
                "distinction": "test_distinction",
                "note": "test_note",

            },
        )
        assert response.status_code == 302
        assert Contributor.objects.filter(first_name="test_firstname").exists()

    def test_view_contributor(self, admin_client, contributor):

        contributor = Contributor.objects.get(first_name='lemire', last_name='dedel', distinction='IT developer')
        url = reverse("admin:contributors_contributor_change", kwargs={"object_id": contributor.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
