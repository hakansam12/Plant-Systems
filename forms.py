from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    PasswordField,
    TextAreaField,
    SelectMultipleField,
    BooleanField,
    FormField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    InputRequired,
    URL,
    Optional,
    NumberRange,
)

TREFLE_COLOR_CHOICES = [
    ("white", "White"),
    ("red", "Red"),
    ("brown", "Brown"),
    ("orange", "Orange"),
    ("yellow", "Yellow"),
    ("lime", "Lime"),
    ("green", "Green"),
    ("cyan", "Cyan"),
    ("blue", "Blue"),
    ("purple", "Purple"),
    ("magenta", "Magenta"),
    ("grey", "Grey"),
    ("black", "Black"),
]
TREFLE_MONTH_CHOICES = [
    ("jan", "JAN"),
    ("feb", "FEB"),
    ("mar", "MAR"),
    ("apr", "APR"),
    ("may", "MAY"),
    ("jun", "JUN"),
    ("jul", "JUL"),
    ("aug", "AUG"),
    ("sep", "SEP"),
    ("oct", "OCT"),
    ("nov", "NOV"),
    ("dec", "DEC"),
]


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class UserEditForm(FlaskForm):
    """Form for editing users."""

    username = StringField("Username")
    email = StringField("E-mail", validators=[Email(), Optional()])
    image_url = StringField("Profile Image URL", validators=[URL(), Optional()])
    password = PasswordField("Current Password", validators=[InputRequired()])


class PlantSearchForm(FlaskForm):
    """Form for searching plants."""

    search = StringField("Search", validators=[Optional()])
    duration = SelectMultipleField(
        "Duration (life cycle)",
        choices=[
            ("annual", "Annual"),
            ("biennial", "Biennial"),
            ("perennial", "Perennial"),
        ],
        validators=[Optional()],
    )
    ligneous_type = SelectMultipleField(
        "Woody Plant Type",
        choices=[
            ("liana", "Liana"),
            ("subshrub", "Subshrub"),
            ("shrub", "Shrub"),
            ("tree", "Tree"),
            ("parasite", "Parasite"),
        ],
        validators=[Optional()],
    )
    flower_color = SelectMultipleField(
        "Flower Color", choices=TREFLE_COLOR_CHOICES, validators=[Optional()],
    )
    growth_months = SelectMultipleField(
        "Growth Months", choices=TREFLE_MONTH_CHOICES, validators=[Optional()],
    )
    bloom_months = SelectMultipleField(
        "Bloom Months", choices=TREFLE_MONTH_CHOICES, validators=[Optional()],
    )
    fruit_months = SelectMultipleField(
        "Fruit Months", choices=TREFLE_MONTH_CHOICES, validators=[Optional()],
    )
    edible_part = SelectMultipleField(
        "Edible Parts",
        choices=[
            ("roots", "Roots"),
            ("stem", "Stem"),
            ("leaves", "Leaves"),
            ("flowers", "Flowers"),
            ("fruits", "Fruits"),
            ("seeds", "Seeds"),
            ("tubers", "Tubers"),
        ],
        validators=[Optional()],
    )
    vegetable = BooleanField("Vegetable", validators=[Optional()])
    evergreen = BooleanField("Evergreen", validators=[Optional()])


class AddProjectForm(FlaskForm):
    """Subform for adding new projects."""

    projects = SelectMultipleField("Connect an existing project:", coerce=int)


class AddPlotForm(FlaskForm):
    """Subform for adding new plots."""

    plots = SelectMultipleField("Connect an existing plot:", coerce=int)


class AddPlantListForm(FlaskForm):
    """Subform for adding new plantlists."""

    plantlists = SelectMultipleField("Connect an existing plant list:", coerce=int)


class ProjectAddForm(FlaskForm):
    """Form for adding new project."""

    name = StringField(
        "Project Name", validators=[DataRequired(message="Project name required.")]
    )
    description = TextAreaField("Description", validators=[Optional()])
    plots = SelectMultipleField("Connect to your your existing plots:", coerce=int)
    plantlists = SelectMultipleField(
        "Connect to your existing plant lists:", coerce=int
    )
    # is_public = BooleanField(
    #     "Would you like this project to be available for other users to copy?",
    #     validators=[Optional()],
    #     default=False,
    # )


class PlantListAddForm(FlaskForm):
    """Form for adding new plant list."""

    name = StringField(
        "Plant List Name",
        validators=[DataRequired(message="Plant List name required.")],
    )
    description = TextAreaField("Description", validators=[Optional()])
    projects = SelectMultipleField("Connect to existing project:", coerce=int)
    plots = SelectMultipleField("Connect to your existing plots:", coerce=int)

    # is_public = BooleanField(
    #     "Would you like this list to be available for other users to copy?",
    #     validators=[Optional()],
    #     default=False,
    # )


class PlotAddForm(FlaskForm):
    """Form for adding new plot."""

    name = StringField(
        "Plot Name", validators=[DataRequired(message="Plot name required.")]
    )
    description = TextAreaField("Description", validators=[Optional()])
    width = IntegerField(
        "Width (to the nearest foot)",
        validators=[
            DataRequired(
                message="Please estimage the plot width to the nearest whole foot."
            ),
            NumberRange(
                min=1,
                max=10,
                message="Width cannot be less than 1 foot or greater than 10 feet.",
            ),
        ],
    )
    length = IntegerField(
        "Length (to the nearest foot)",
        validators=[
            DataRequired(
                message="Please estimage the plot length to the nearest whole foot."
            ),
            NumberRange(
                min=1,
                max=50,
                message="Width cannot be less than 1 foot or greater than 50 feet.",
            ),
        ],
    )
    projects = SelectMultipleField("Add to existing project:", coerce=int)
    plantlists = SelectMultipleField(
        "Connect to your existing plant lists:", coerce=int
    )

    # is_public = BooleanField(
    #     "Would you like this list to be available for other users to copy?",
    #     validators=[Optional()],
    #     default=False,
    # )
