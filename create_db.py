from applications import db
from applications.models import TVShow

def delete_database():
    db.drop_all()

def create_database():
    db.create_all()
    
def add_entries():
    entry1 = TVShow(title="Doctor Who", genre="Sci-Fi", rating="5", image_url="https://m.media-amazon.com/images/I/61vLddwKXTL._AC_SY741_.jpg")
    entry2 = TVShow(title="Sherlock", genre="Crime", rating="4", image_url="https://static.posters.cz/image/750/posters/sherlock-series-4-iconic-i33910.jpg")
    entry3 = TVShow(title="The Expanse", genre="Sci-Fi", rating="4", image_url="https://resizing.flixster.com/a7VRb-2Xh__4_-Avt3x4qCdguzQ=/ems.cHJkLWVtcy1hc3NldHMvdHZzZWFzb24vUlRUVjU3ODk2OS53ZWJw")
    entry4 = TVShow(title="Game of Thrones", genre="Fantasy", rating="3", image_url="https://flxt.tmsimg.com/assets/p8553063_b_v13_ax.jpg")
    db.session.add(entry1)
    db.session.add(entry2)
    db.session.add(entry3)
    db.session.add(entry4)
    db.session.commit()
    
def see_db_entries():
    entries = TVShow.query.all()
    for entry in entries:
        print(f"{entry.title}, {entry.genre}, {entry.rating}, {entry.date}")

if __name__ == '__main__':
    delete_database()
    create_database()
    add_entries()
    see_db_entries()