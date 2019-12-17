from django.core.management.base import BaseCommand
from django.utils.encoding import smart_str

from userena.models import UserenaSignup

arguments = (
    (
        "--no-output",
        {
            "action": "store_false",
            "dest": "output",
            "default": True,
            "help": "Hide informational output.",
        },
    ),
    (
        "--test",
        {
            "action": "store_true",
            "dest": "test",
            "default": False,
            "help": "Displays that it's testing management command. Don't use it yourself.",
        },
    ),
)


class Command(BaseCommand):
    """
    For unknown reason, users can get wrong permissions.
    This command checks that all permissions are correct.

    """

    def add_arguments(self, parser):
        for arg, attrs in arguments:
            parser.add_argument(arg, **attrs)

    help = "Check that user permissions are correct."

    def handle(self, **options):
        permissions, users, warnings = UserenaSignup.objects.check_permissions()
        output = options.pop("output")
        test = options.pop("test")
        if test:
            self.stdout.write(40 * ".")
            self.stdout.write(
                "\nChecking permission management command. Ignore output..\n\n"
            )
        if output:
            for p in permissions:
                self.stdout.write("Added permission: %s\n" % p)

            for u in users:
                self.stdout.write(
                    "Changed permissions for user: %s\n"
                    % smart_str(u, encoding="utf-8", strings_only=False)
                )

            for w in warnings:
                self.stdout.write("WARNING: %s\n" % w)

        if test:
            self.stdout.write("\nFinished testing permissions command.. continuing..\n")
