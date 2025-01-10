import 'package:flutter/material.dart';
import 'package:together/src/model/announcement.dart';
import 'package:together/src/presentation/announcement/announcement_details.dart';
import 'package:intl/intl.dart';

class AnnouncementsScreen extends StatefulWidget {
  const AnnouncementsScreen({super.key});

  @override
  _AnnouncementsScreenState createState() => _AnnouncementsScreenState();
}

class _AnnouncementsScreenState extends State<AnnouncementsScreen> {
  List<Announcement> announcements = [
    Announcement(
      task: 'Сходить в магазин',
      city: 'Минск',
      address: 'ул. Победы, д. 10',
      desiredDate: DateTime.now(),
    ),
    Announcement(
      task: 'Заполнить документы',
      city: 'Гродно',
      address: 'ул. Советская, д. 15',
      desiredDate: DateTime.now().add(const Duration(days: 1)),
    ),
    Announcement(
      task: 'Помочь с продуктами',
      city: 'Гродно',
      address: 'ул. Советская, д. 15',
      desiredDate: DateTime.now().add(const Duration(days: 2)),
    ),
    Announcement(
      task: 'Помочь с ем то там',
      city: 'Гродно',
      address: 'ул. Советская, д. 15',
      desiredDate: DateTime.now().add(const Duration(days: 3)),
    ),
    Announcement(
      task: 'КТо готов помочь',
      city: 'Гродно',
      address: 'ул. Советская, д. 15',
      desiredDate: DateTime.now().add(const Duration(days: 4)),
    ),
  ];

  List<Announcement> filteredAnnouncements = [];
  final TextEditingController _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    filteredAnnouncements = announcements;
    _searchController.addListener(_filterAnnouncements);
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }


  void _filterAnnouncements() {
    String query = _searchController.text.toLowerCase();
    setState(() {
      filteredAnnouncements = announcements.where((announcement) {
        return announcement.task.toLowerCase().contains(query); 
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Объявления'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildSearchBar(),
            const SizedBox(height: 16),
            _buildActionButtons(),
            const SizedBox(height: 16),
            _buildAnnouncementsList(),
          ],
        ),
      ),
    );
  }


  Widget _buildSearchBar() {
    return TextField(
      controller: _searchController,
      decoration: InputDecoration(
        hintText: 'Поиск',
        prefixIcon: const Icon(Icons.search),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(16),
        ),
        filled: true,
        fillColor: Colors.white,
      ),
    );
  }


  Widget _buildActionButtons() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        ElevatedButton.icon(
          onPressed: () {},
          icon: const Icon(Icons.sort),
          label: const Text('Сортировать'),
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16),
            ),
          ),
        ),
        ElevatedButton.icon(
          onPressed: () {},
          icon: const Icon(Icons.filter_alt),
          label: const Text('Фильтр'),
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16),
            ),
          ),
        ),
      ],
    );
  }


  Widget _buildAnnouncementsList() {
    return Expanded(
      child: ListView.builder(
        itemCount: filteredAnnouncements.length,
        itemBuilder: (context, index) {
          final announcement = filteredAnnouncements[index];
          return Padding(
            padding: const EdgeInsets.only(bottom: 8.0),
            child: AnnouncementCard(
              announcement: announcement,
            ),
          );
        },
      ),
    );
  }
}

class AnnouncementCard extends StatelessWidget {
  final Announcement announcement;

  const AnnouncementCard({
    super.key,
    required this.announcement,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => AnnouncementDetailScreen(announcement: announcement),
          ),
        );
      },
      child: Container(
        decoration: BoxDecoration(
          color: Colors.lightBlue[50],
          borderRadius: BorderRadius.circular(16),
        ),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildTitle(),
              const SizedBox(height: 8),
              _buildDateAndAddress(),
              const SizedBox(height: 8),
              _buildDescription(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTitle() {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),
      decoration: BoxDecoration(
        color: Colors.lightBlue[100],
        borderRadius: BorderRadius.circular(8),
      ),
      child: const Text(
        'Объявление',
        style: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }

  Widget _buildDateAndAddress() {
    final formattedDate = DateFormat('d MMMM').format(announcement.desiredDate);

    return Row(
      children: [
        Expanded(
          child: Container(
            padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(
                color: Colors.grey[300]!,
                width: 1.5,
              ),
            ),
            child: Text(
              formattedDate,
              style: const TextStyle(fontSize: 16),
              overflow: TextOverflow.ellipsis,
            ),
          ),
        ),
        const SizedBox(width: 8),
        Expanded(
          child: Container(
            padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(
                color: Colors.grey[300]!,
                width: 1.5,
              ),
            ),
            child: Text(
              announcement.address,
              style: const TextStyle(fontSize: 14),
              overflow: TextOverflow.ellipsis,
            ),
          ),
        ),
      ],
    );
  }

  
  Widget _buildDescription() {
    return Text(
      announcement.task,
      style: const TextStyle(fontSize: 16),
    );
  }
}
