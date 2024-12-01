import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:together/src/presentation/announcement/announcements.dart';
import 'package:together/src/presentation/create_announcement/create_announcement.dart';
import 'package:together/src/presentation/registration/ui/login.dart';
import 'package:together/src/presentation/registration/user/user.dart';

class MainScreen extends StatelessWidget {
  final User? currentUser; 

  const MainScreen({Key? key, required this.currentUser}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    if (currentUser == null || currentUser!.role == Role.UNKNOWN) {
      log(currentUser!.role.toString());
      return LoginScreen();
    }

    switch (currentUser!.role) {
      case Role.VOLUNTEER:
        return AnnouncementsScreen();
      case Role.NEEDY:
        return CreateAnnouncementScreen();
      default:
        return LoginScreen();
    }
  }
}
