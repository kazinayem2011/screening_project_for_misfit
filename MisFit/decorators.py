from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def login_required(session_key, fail_redirect_to):
    def _session_required(view_func):
        @wraps(view_func)
        def __session_required(request, *args, **kwargs):
            try:
                session = request.session.get(session_key)
                if session is None:
                    raise ValueError('You Are Not Logged In!')
            except KeyError as e:
                messages.error(request, 'You Are Not Logged In!')
                return redirect(fail_redirect_to)
            # Commented by nayem . . .
            # except ValueError as e:
            #     messages.error(request, e.message)

            except ValueError:
                messages.error(request, 'You Are Not Logged In!')
                return redirect(fail_redirect_to)
            else:
                return view_func(request, *args, **kwargs)
        return __session_required
    return _session_required