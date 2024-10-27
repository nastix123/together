import 'package:flutter/material.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text("Добро пожаловать"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Center(
              child: Image.asset(
                'assets/images/logo.png',
                height: 100,
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Наша миссия - помогать тем, кто нуждается в поддержке и заботе. '
              'Мы стремимся объединить волонтеров и нуждающихся, чтобы сделать мир лучше.',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/volunteer-registration');
              },
              child: const Text("Регистрация волонтера"),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/needy-registration');
              },
              child: const Text("Регистрация нуждающегося"),
            ),
            const SizedBox(height: 10),
            OutlinedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/login');
              },
              child: const Text("Вход в аккаунт"),
            ),
            const SizedBox(height: 20),
            TextButton(
              onPressed: () {
                Navigator.pushNamed(context, '/contacts');
              },
              child: const Text("Контакты"),
            ),
            TextButton(
              onPressed: () {
                Navigator.pushNamed(context, '/user-agreement');
              },
              child: const Text("Пользовательское соглашение"),
            ),
          ],
        ),
      ),
    );
  }
}
