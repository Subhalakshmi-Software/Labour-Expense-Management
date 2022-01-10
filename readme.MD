```sh

docker build -t labour_expense_management:latest .

docker run -d \
    -p 8000:8000 \
    -v $(pwd)/db.sqlite3:/code/db.sqlite3 \
    labour_expense_management:latest

docker exec -it 87fc80e2e68e bash

git clone https://github.com/Subhalakshmi-Software/Labour-Expense-Management.git

```