import 'package:flutter/material.dart';
import 'package:together/src/domain/announcement.dart';

class AnnouncementDetailScreen extends StatelessWidget {
  final Announcement announcement;

  const AnnouncementDetailScreen({super.key, required this.announcement});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Детали объявления',
          style: TextStyle(fontSize: 22), 
        ),
        backgroundColor: Colors.blueAccent,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildTask(),
            const SizedBox(height: 16),
            _buildDateAndAddress(),
            const SizedBox(height: 16),
            _buildPreferences(),
            const SizedBox(height: 16),
            _buildComments(),
            const SizedBox(height: 20),
            _buildStartButton(context),
          ],
        ),
      ),
    );
  }


  Widget _buildTask() {
    return Text(
      announcement.task,
      style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.blueAccent),
    );
  }


  Widget _buildDateAndAddress() {
    return Row(
      children: [
        _buildChip(label: 'Дата: ${announcement.desiredDate.toLocal().toString().split(' ')[0]}'),
        const SizedBox(width: 16),
        _buildChip(label: 'Адрес: ${announcement.address}'),
      ],
    );
  }


  Widget _buildChip({required String label}) {
    return Chip(
      label: Text(
        label,
        style: const TextStyle(color: Colors.white),
      ),
      backgroundColor: Colors.blueAccent,
    );
  }

  
  Widget _buildPreferences() {
    final preferences = [
      'Пол: ${announcement.genderPreference}',
      'Возраст: ${announcement.agePreference ?? 'Не указан'}',
      'Рейтинг: ${announcement.ratingPreference ?? 'Не указан'}',
    ];
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: preferences.map((pref) => Padding(
        padding: const EdgeInsets.symmetric(vertical: 4.0),
        child: Text(
          pref,
          style: const TextStyle(fontSize: 16, color: Colors.black54),
        ),
      )).toList(),
    );
  }

  // Строим комментарии
  Widget _buildComments() {
    return Text(
      'Комментарии: ${announcement.comments ?? 'Нет комментариев'}',
      style: const TextStyle(fontSize: 16, color: Colors.black54),
    );
  }

  // Кнопка "Приступить к работе"
  Widget _buildStartButton(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
      
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const WorkStartScreen()),
        );
      },
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.blueAccent, 
        padding: const EdgeInsets.symmetric(vertical: 12.0, horizontal: 24.0),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      ),
      child: const Text(
        'Приступить к работе',
        style: TextStyle(fontSize: 18, color: Colors.white),
      ),
    );
  }
}

class WorkStartScreen extends StatelessWidget {
  const WorkStartScreen();
  
  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body:Card(
        child: Text("Start Wotk")
      )
    );
  }
}
