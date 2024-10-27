
import 'package:file_picker/file_picker.dart';
import 'dart:io';
import 'package:flutter/material.dart';

class RegistrationNeedyStep1 extends StatefulWidget {


  final VoidCallback onNext;

  const RegistrationNeedyStep1({required this.onNext});

  @override
  _RegistrationNeedyStep1State createState() => _RegistrationNeedyStep1State();
}

class _RegistrationNeedyStep1State extends State<RegistrationNeedyStep1> {
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
      appBar: AppBar(title: const Text("Регистрация нуждающегося - Шаг 1")),
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



class RegistrationNeedyStep2 extends StatefulWidget {
  final VoidCallback onFinish;

  const RegistrationNeedyStep2({required this.onFinish});

  @override
  _RegistrationNeedyStep2State createState() => _RegistrationNeedyStep2State();
}

class _RegistrationNeedyStep2State extends State<RegistrationNeedyStep2> {
  final List<File> _selectedDocuments = [];

  Future<void> _pickDocument() async {
    final result = await FilePicker.platform.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['pdf', 'jpg', 'jpeg', 'png'],
      allowMultiple: true,
    );

    if (result != null) {
      setState(() {
        _selectedDocuments.addAll(
          result.files.map((file) => File(file.path!)),
        );
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Регистрация нуждающегося - Шаг 2")),
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

            ElevatedButton.icon(
              onPressed: _pickDocument,
              icon: const Icon(Icons.upload_file),
              label: const Text('Загрузить документ'),
            ),

            const SizedBox(height: 10),
            Expanded(
              child: ListView.builder(
                itemCount: _selectedDocuments.length,
                itemBuilder: (context, index) {
                  final fileName = _selectedDocuments[index].path.split('/').last;
                  return ListTile(
                    leading: const Icon(Icons.insert_drive_file),
                    title: Text(fileName),
                    trailing: IconButton(
                      icon: const Icon(Icons.delete, color: Colors.red),
                      onPressed: () {
                        setState(() {
                          _selectedDocuments.removeAt(index);
                        });
                      },
                    ),
                  );
                },
              ),
            ),

            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: widget.onFinish,
              child: const Text('Завершить регистрацию'),
            ),
          ],
        ),
      ),
    );
  }
}

class NeedyRegistrationScreen extends StatelessWidget {
    static const routeName = "/needy-registration";

  
  @override
  Widget build(BuildContext context) {
    return RegistrationNeedyStep1(
      onNext: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => RegistrationNeedyStep2(
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