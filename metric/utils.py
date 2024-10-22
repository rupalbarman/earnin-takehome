from metric.models import Metric


def create_inital_metrics() -> None:
    METRICS = [
        {"slug": "visitors", "name": "Visitors per day"},
        {"slug": "impressions", "name": "Impressions"},
        {"slug": "number_of_clicks", "name": "Number of clicks"},
        {"slug": "unique_visitor_country", "name": "Unique visitors by country"},
        {"slug": "age", "name": "Age of page"},
        {"slug": "colors", "name": "Colors per day"},
    ]

    metrics = [Metric(**data) for data in METRICS]

    Metric.objects.bulk_create(metrics, batch_size=100, ignore_conflicts=True)
