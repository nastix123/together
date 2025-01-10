import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:together/src/model/user.dart';
import 'package:together/src/network/network_service.dart';
import 'package:together/src/utils/exceptions/form_exceptions.dart';

part 'login_event.dart';
part 'login_state.dart';

class LoginBloc extends Bloc<LoginEvent, LoginState> {
  LoginBloc() : super(LoginFormState()) {
    on<LoginRequestEvent>((event, emit) async {
      emit(LoginLoadingState());
      try {
        final user = await AuthService.login(
          email: event.email,
          password: event.password,
        );
        emit(LoginSuccessState(
          user,
        ));
      } on FormGeneralException catch (e) {
        emit(LoginErrorState(e));
      } on FormFieldsException catch (e) {
        emit(LoginErrorState(e));
      } catch (e) {
        emit(LoginErrorState(
          FormGeneralException(message: 'Unidentified error'),
        ));
      }
    });
  }
}
