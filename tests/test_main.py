import pytest

def test_homepage(client):
    response = client.get("/book-all")
    assert response.status_code == 200


@pytest.fixture
def create_book(client):
    def _create_book(title:str, description:str, completed:bool):
        data={
        "title": title,
        "description": description,
        "completed": completed
        }
        response=client.post('/book-add',json=data)
        return response.json()
    return _create_book

@pytest.fixture
def delete_book(client):
    def _delete_book(book_id:int):
        response=client.delete(f'/book-delete/{book_id}')
        return response

    return _delete_book

@pytest.fixture
def get_book(client):
    def _get_book(get_book_id):
        response=client.get(f'/book/{get_book_id}')

        return response
    return _get_book

def test_book_delete(client,create_book,delete_book):
    book=create_book('Test','Test-description',True)
    assert book['title']=='Test'
    assert book['description']=='Test-description'
    assert book['completed']==True
    delete_book(book['id'])

def test_book_get(create_book, get_book, delete_book):
    book = create_book('Test', 'Test-description', True)
    get_book_id = book['id']
    response = get_book(get_book_id)

    assert response.status_code == 200
    get_book_data = response.json()

    assert get_book_data['title'] == 'Test'
    assert get_book_data['description'] == 'Test-description'
    assert get_book_data['completed'] == True

    response_delete = delete_book(get_book_id)

    assert response_delete.status_code == 200


def test_book_update(client,create_book,delete_book):
    add_book=create_book('test_1','test_2',True)
    print(add_book,'Book information')

    data={
    "title": "title update",
    "description": "description update",
    "completed": True
    }

    book_id=add_book['id']
    response=client.patch(f'/book-update/{book_id}',json=data)
    assert response.status_code==200,'An error occurred while updating the book.'
    delete_book(book_id)
