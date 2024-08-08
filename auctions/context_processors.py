def get_user_watchlist_length(request):
    return {
        'watchlist_length': len(request.user.watchlist.all())
    }