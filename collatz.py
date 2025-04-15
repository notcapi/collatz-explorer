import csv

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def generate_collatz_data(limit):
    data = []
    for i in range(1, limit + 1):
        sequence = collatz_sequence(i)
        data.append({
            'start': i,
            'steps': len(sequence) - 1,
            'max_value': max(sequence)
        })
    return data

def save_to_csv(data, filename='collatz_data.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['start', 'steps', 'max_value'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    limit = 1000  # Puedes cambiar esto a 10000, 50000, etc.
    print(f"Generando secuencias Collatz desde 1 hasta {limit}...")
    collatz_data = generate_collatz_data(limit)
    save_to_csv(collatz_data)
    print("¡Datos guardados en collatz_data.csv!")
