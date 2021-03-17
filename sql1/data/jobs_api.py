import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)


@blueprint.route("/api/jobs")
def get_jobs():
    session = db_session.create_session()
    news = session.query(Jobs).all()
    return jsonify(
        {
            "jobs":
                [item.to_dict(only=("id", "jobs", "team_leader", "work_size",
                                    "start_date", "end_date", "is_finished",
                                    "category"))
                 for item in news]
        }
    )
