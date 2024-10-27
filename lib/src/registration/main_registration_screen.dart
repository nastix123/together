import 'package:flutter/material.dart';
import '../registration/registration_view.dart';

class VolunteerRegistrationScreen extends StatelessWidget {
  static const routeName = '/volunteer-registration';

  @override
  Widget build(BuildContext context) {
    return RegistrationStep1(
      onNext: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => RegistrationStep2(
              onFinish: () {
                Navigator.popUntil(context, (route) => route.isFirst);
              },
            ),
          ),
        );
      },
    );
  }
}


