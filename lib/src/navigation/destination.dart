enum Destination { welcome, volunteerRegistration, needyRegistration, volunteerDashboard, needyDashboard }

extension DestinationExtension on Destination {
  String get route {
    switch (this) {
      case Destination.welcome:
        return '/welcome';
      case Destination.volunteerRegistration:
        return '/registration';;
      case Destination.volunteerDashboard:
        return '/volunteer-dashboard';
      case Destination.needyDashboard:
        return '/needy-dashboard';
      default:
        return '';
    }
  }
}
