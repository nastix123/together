import 'package:flutter/material.dart';

class Announcement {
  final String task;
  final String city;
  final String address;
  final DateTime desiredDate;
  final TimeOfDay? startTime;
  final TimeOfDay? endTime;
  final String? genderPreference;
  final String? agePreference;
  final double? ratingPreference;
  final String? comments;
  AnnouncementStatus status;

  Announcement({
    required this.task,
    required this.city,
    required this.address,
    required this.desiredDate,
    this.startTime,
    this.endTime,
    this.genderPreference,
    this.agePreference,
    this.ratingPreference,
    this.comments,
    this.status = AnnouncementStatus.newStatus,
  });

  String formatTime(TimeOfDay? time, BuildContext context) {
    if (time == null) return '';
    return time.format(context);
  }
}

enum AnnouncementStatus {
  newStatus, // Новое
  accepted, // Принято
  completed, // Выполнено
  notCompleted, // Не выполнено
  outdated, // Не актуально
  declined, // Отклонено
}

extension AnnouncementStatusExtension on AnnouncementStatus {
  String get label {
    switch (this) {
      case AnnouncementStatus.newStatus:
        return 'Новое';
      case AnnouncementStatus.accepted:
        return 'Принято';
      case AnnouncementStatus.completed:
        return 'Выполнено';
      case AnnouncementStatus.notCompleted:
        return 'Не выполнено';
      case AnnouncementStatus.outdated:
        return 'Не актуально';
      case AnnouncementStatus.declined:
        return 'Отклонено';
    }
  }
}
