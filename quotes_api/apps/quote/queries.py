def votes_projection(device_id):
    return {
            '$project': {
                '_id': '$_id',
                'content': '$content',
                'ups_count': '$ups_count',
                'downs_count': '$downs_count',
                'comments_count': '$comments_count',
                'date': '$date',
                'author': '$author',
                'enabled': '$enabled',
                'days_to_die': '$days_to_die',
                'background_color': '$background_color',
                'font_family': '$font_family',
                'ups': {
                    '$in': [device_id, '$ups']
                },
                'downs': {
                    '$in': [device_id, '$downs']
                }, 
                'votes': '$votes'
            }
        }
    
def searc_match(query):
    return {
            '$match': {
                '$or': [
                    {'author': {'$regex': query}},
                    {'content': {'$regex': query}},
                ]
            }
        }