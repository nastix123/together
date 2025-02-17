import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:together/src/model/user.dart';
import 'package:together/src/network/network_service.dart';
import 'package:together/src/utils/exceptions/form_exceptions.dart';

part 'register_event.dart';
part 'register_state.dart';

class RegisterBloc extends Bloc<RegisterEvent, RegisterState> {
  RegisterBloc() : super(RegisterFormState()) {
    on<RegisterRequestEvent>((event, emit) async {
      emit(RegisterLoadingState());
      try {
        final user = await AuthService.register(
          email: event.email,
          password: event.password,
          cellphone: event.cellphone,
          firstName: event.firstName,
          lastName: event.lastName,
        );
        emit(RegisterSuccessState(
          user,
        ));
      } on FormGeneralException catch (e) {
        emit(RegisterErrorState(e));
      } on FormFieldsException catch (e) {
        emit(RegisterErrorState(e));
      } catch (e) {
        emit(RegisterErrorState(
          FormGeneralException(message: 'Unidentified error'),
        ));
      }
    });
  }
}
