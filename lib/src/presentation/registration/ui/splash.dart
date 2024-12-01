import 'package:flutter/material.dart';
import 'package:together/src/presentation/registration/ui/main.dart';
import 'package:together/src/presentation/registration/user/user.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  User? currentUser;

  @override
  void initState() {
    super.initState();
    _checkUserStatus();
  }

  Future<void> _checkUserStatus() async {

    final storedUser = await loadUserFromStorage();

    
    setState(() {
      currentUser = storedUser;
    });

  
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => MainScreen(currentUser: currentUser),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(
        child: CircularProgressIndicator(), 
      ),
    );
  }
}

Future<User?> loadUserFromStorage() async {
  
  await Future.delayed(const Duration(seconds: 2));
  return User(
    id: '123',
    role: Role.UNKNOWN, 
    name: 'John',
    surname: 'Doe',
    city: 'Minsk',
    email: 'john.doe@example.com',
  );
}

