import 'package:flutter/material.dart';

class RegistrationStep1 extends StatefulWidget {
  final VoidCallback onNext;

  const RegistrationStep1({required this.onNext});

  @override
  _RegistrationStep1State createState() => _RegistrationStep1State();
}

class _RegistrationStep1State extends State<RegistrationStep1> {
  final _formKey = GlobalKey<FormState>();
  final _phoneController = TextEditingController(text: '+375');
  final _emailController = TextEditingController();

  @override
  void dispose() {
    _phoneController.dispose();
    _emailController.dispose();
    super.dispose();
  }

  String? _validatePhone(String? value) {
    final phonePattern = RegExp(r'^\+375\d{9}$');
    if (!phonePattern.hasMatch(value ?? '')) {
      return 'Введите корректный номер (+375XXXXXXXXX)';
    }
    return null;
  }

  String? _validateEmail(String? value) {
    final emailPattern = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
    if (!emailPattern.hasMatch(value ?? '')) {
      return 'Введите корректный email';
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Регистрация волонтера - Шаг 1")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              const TextField(
                decoration: InputDecoration(labelText: 'Фамилия'),
              ),
              const SizedBox(height: 10),
              const TextField(
                decoration: InputDecoration(labelText: 'Имя'),
              ),
              const SizedBox(height: 10),
              Tooltip(
                message: 'Введите номер в формате +375XXXXXXXXX',
                child: TextFormField(
                  controller: _phoneController,
                  decoration: const InputDecoration(labelText: 'Телефон'),
                  keyboardType: TextInputType.phone,
                  validator: _validatePhone,
                ),
              ),
              const TextField(
                decoration: InputDecoration(labelText: 'Город'),
              ),
              const SizedBox(height: 10),
              Tooltip(
                message: 'Введите корректный email',
                child: TextFormField(
                  controller: _emailController,
                  decoration: const InputDecoration(labelText: 'Email'),
                  keyboardType: TextInputType.emailAddress,
                  validator: _validateEmail,
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    widget.onNext();
                  }
                },
                child: const Text('Продолжить'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}


class RegistrationStep2 extends StatelessWidget {
  final VoidCallback onFinish;

  const RegistrationStep2({required this.onFinish});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Регистрация волонтера - Шаг 2")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            const TextField(
              decoration: InputDecoration(labelText: 'Серия паспорта'),
            ),
            const TextField(
              decoration: InputDecoration(labelText: 'Номер паспорта'),
            ),
            const TextField(
              decoration: InputDecoration(labelText: 'Кем выдан'),
            ),
            const TextField(
              decoration: InputDecoration(labelText: 'Дата выдачи'),
              keyboardType: TextInputType.datetime,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: onFinish,
              child: const Text('Завершить регистрацию'),
            ),
          ],
        ),
      ),
    );
  }
}



