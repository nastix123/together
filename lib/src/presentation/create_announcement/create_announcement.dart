import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:together/src/model/announcement.dart';

class CreateAnnouncementScreen extends StatefulWidget {
  final Announcement? announcement;

  const CreateAnnouncementScreen({Key? key, this.announcement}) : super(key: key);

  @override
  _CreateAnnouncementScreenState createState() => _CreateAnnouncementScreenState();
}

class _CreateAnnouncementScreenState extends State<CreateAnnouncementScreen> {
  final _formKey = GlobalKey<FormState>();
  late TextEditingController _taskController;
  late TextEditingController _addressController;
  late TextEditingController _commentsController;
  late DateTime _desiredDate;
  late TimeOfDay _startTime;
  late TimeOfDay _endTime;
  String? _genderPreference;
  String? _agePreference;
  double? _ratingPreference;
  AnnouncementStatus _status = AnnouncementStatus.newStatus;

  @override
  void initState() {
    super.initState();
    _taskController = TextEditingController();
    _addressController = TextEditingController();
    _commentsController = TextEditingController();

    if (widget.announcement != null) {
      _taskController.text = widget.announcement!.task;
      _addressController.text = widget.announcement!.address;
      _commentsController.text = widget.announcement!.comments ?? '';
      _desiredDate = widget.announcement!.desiredDate;
      _startTime = widget.announcement!.startTime ?? TimeOfDay.now();
      _endTime = widget.announcement!.endTime ?? TimeOfDay.now();
      _genderPreference = widget.announcement!.genderPreference;
      _agePreference = widget.announcement!.agePreference;
      _ratingPreference = widget.announcement!.ratingPreference;
      _status = widget.announcement!.status;
    } else {
      _desiredDate = DateTime.now();
      _startTime = TimeOfDay.now();
      _endTime = TimeOfDay.now();
    }
  }

  @override
  void dispose() {
    _taskController.dispose();
    _addressController.dispose();
    _commentsController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Создание объявления'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                _buildTextField(
                  controller: _taskController,
                  label: 'Задача',
                  hintText: 'Введите задачу',
                  validator: (value) => value!.isEmpty ? 'Введите задачу' : null,
                ),
                const SizedBox(height: 16),
                _buildTextField(
                  controller: _addressController,
                  label: 'Адрес',
                  hintText: 'Введите адрес',
                  validator: (value) => value!.isEmpty ? 'Введите адрес' : null,
                ),
                const SizedBox(height: 16),
                _buildDateTimePickers(),
                const SizedBox(height: 16),
                _buildGenderPreferenceField(),
                const SizedBox(height: 16),
                _buildAgePreferenceField(),
                const SizedBox(height: 16),
                _buildRatingPreferenceField(),
                const SizedBox(height: 16),
                _buildCommentsField(),
                const SizedBox(height: 16),
                _buildStatusDropdown(),
                const SizedBox(height: 24),
                Center(
                  child: ElevatedButton(
                    onPressed: _submitForm,
                    style: ElevatedButton.styleFrom(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                      padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 16),
                    ),
                    child: const Text('Создать объявление'),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    required String hintText,
    String? Function(String?)? validator,
  }) {
    return TextFormField(
      controller: controller,
      decoration: InputDecoration(
        labelText: label,
        hintText: hintText,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      validator: validator,
    );
  }

  Widget _buildDateTimePickers() {
    return Row(
      children: [
        Expanded(
          child: GestureDetector(
            onTap: () => _pickDate(context),
            child: AbsorbPointer(
              child: TextFormField(
                decoration: InputDecoration(
                  labelText: 'Дата',
                  hintText: DateFormat('dd.MM.yyyy').format(_desiredDate),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),
            ),
          ),
        ),
        const SizedBox(width: 16),
        Expanded(
          child: GestureDetector(
            onTap: () => _pickStartTime(context),
            child: AbsorbPointer(
              child: TextFormField(
                decoration: InputDecoration(
                  labelText: 'Время начала',
                  hintText: _startTime.format(context),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }

  Future<void> _pickDate(BuildContext context) async {
    final pickedDate = await showDatePicker(
      context: context,
      initialDate: _desiredDate,
      firstDate: DateTime(2000),
      lastDate: DateTime(2100),
    );
    if (pickedDate != null && pickedDate != _desiredDate) {
      setState(() {
        _desiredDate = pickedDate;
      });
    }
  }

  Future<void> _pickStartTime(BuildContext context) async {
    final pickedTime = await showTimePicker(
      context: context,
      initialTime: _startTime,
    );
    if (pickedTime != null) {
      setState(() {
        _startTime = pickedTime;
      });
    }
  }

  Widget _buildGenderPreferenceField() {
    return DropdownButtonFormField<String>(
      value: _genderPreference,
      hint: const Text('Выберите пол'),
      items: ['Мужчина', 'Женщина', 'Не имеет значения']
          .map((label) => DropdownMenuItem<String>(
                value: label,
                child: Text(label),
              ))
          .toList(),
      onChanged: (value) {
        setState(() {
          _genderPreference = value;
        });
      },
      decoration: InputDecoration(
        labelText: 'Предпочтения по полу',
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }

  Widget _buildAgePreferenceField() {
    return DropdownButtonFormField<String>(
      value: _agePreference,
      hint: const Text('Выберите возраст'),
      items: ['18-30', '31-50', '50+']
          .map((label) => DropdownMenuItem<String>(
                value: label,
                child: Text(label),
              ))
          .toList(),
      onChanged: (value) {
        setState(() {
          _agePreference = value;
        });
      },
      decoration: InputDecoration(
        labelText: 'Предпочтения по возрасту',
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }

  Widget _buildRatingPreferenceField() {
    return TextFormField(
      keyboardType: TextInputType.number,
      decoration: InputDecoration(
        labelText: 'Предпочтительный рейтинг',
        hintText: 'Введите рейтинг',
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      onChanged: (value) {
        _ratingPreference = double.tryParse(value);
      },
    );
  }

  Widget _buildCommentsField() {
    return TextFormField(
      controller: _commentsController,
      maxLines: 4,
      decoration: InputDecoration(
        labelText: 'Комментарии',
        hintText: 'Введите дополнительные комментарии',
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }

  Widget _buildStatusDropdown() {
    return DropdownButtonFormField<AnnouncementStatus>(
      value: _status,
      items: AnnouncementStatus.values.map((status) {
        return DropdownMenuItem<AnnouncementStatus>(
          value: status,
          child: Text(status.toString().split('.').last),
        );
      }).toList(),
      onChanged: (value) {
        setState(() {
          _status = value!;
        });
      },
      decoration: InputDecoration(
        labelText: 'Статус объявления',
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    );
  }

  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      final newAnnouncement = Announcement(
        task: _taskController.text,
        address: _addressController.text,
        desiredDate: _desiredDate,
        startTime: _startTime,
        endTime: _endTime,
        genderPreference: _genderPreference,
        agePreference: _agePreference,
        ratingPreference: _ratingPreference,
        comments: _commentsController.text,
        status: _status, 
        city: _addressController.text,
      );
      // Обработка сохранения нового объявления
      Navigator.pop(context, newAnnouncement);
    }
  }
}
