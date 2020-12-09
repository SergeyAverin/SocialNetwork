def add_voted(model, filter, voted):
    publication = model.objects.get(**filter)
    
    if voted == 'down':
        publication.downvoted += 1
    elif voted == 'up':
        publication.upvoted += 1

    publication.save()
    
    return publication