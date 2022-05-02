def votes_projection(device_id):
    return {
            '$project': {
                '_id': '$_id',
                'content': '$content',
                'original_quote': '$original_quote',
                'comments': '$comments',
                'comments_count': '$comments_count',
                'date': '$date',
                
                'ups': {
                    '$in': [device_id, '$ups']
                },
                'downs': {
                    '$in': [device_id, '$downs']
                }, 
                'votes': '$votes'
            }
        }