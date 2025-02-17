import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:together/src/presentation/announcement/announcements.dart';
import 'package:together/src/presentation/create_announcement/create_announcement.dart';
import 'package:together/src/presentation/registration/ui/registration.dart';
import 'package:together/src/presentation/registration/ui/splash.dart';
import 'settings/settings_controller.dart';

class MyApp extends StatelessWidget {
  const MyApp({
    super.key,
    required this.settingsController,
  });

  final SettingsController settingsController;

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: settingsController,
      builder: (BuildContext context, Widget? child) {
        return MaterialApp(
          debugShowCheckedModeBanner: false,
          restorationScopeId: 'app',
          localizationsDelegates: const [
            AppLocalizations.delegate,
            GlobalMaterialLocalizations.delegate,
            GlobalWidgetsLocalizations.delegate,
            GlobalCupertinoLocalizations.delegate,
          ],
          supportedLocales: const [
            Locale('en', ''),
          ],
          onGenerateTitle: (BuildContext context) =>
              AppLocalizations.of(context)!.appTitle,
          theme: ThemeData(),
          darkTheme: ThemeData.dark(),
          themeMode: settingsController.themeMode,
          home: const SplashScreen(),
          routes: {
            '/register': (context) => RegistrationScreen(),
            '/announcements': (context) => const AnnouncementsScreen(),
            '/create_announcement': (context) =>
                const CreateAnnouncementScreen()
          },
        );
      },
    );
  }
}
