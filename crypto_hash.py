import hashlib
import json


def crypto_hash(data):
  """
  Return a sha-256 of the given data.
  """
  stingified_data = json.dumps(data)

  return hashlib.sha256(stingified_data.encode('utf-8')).hexdigest()


def main():
  print(f"crypto_hash(1): {crypto_hash(1)}")


if __name__ == '__main__':
  main()