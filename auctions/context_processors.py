def get_user_watchlist_length(request):
    if request.user.is_authenticated:
        return {
            'watchlist_length': len(request.user.watchlist.all())
        }
    else:
        return {
            'watchlist_length': 0
        }