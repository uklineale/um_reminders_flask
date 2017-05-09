echo "app password?"
read pw
export UM_PASSWORD=$pw

echo "bandwidth username?"
read user
export UM_USERNAME=$user

echo "bandwidth token?"
read token
export UM_TOKEN=$token

echo "bandwidth secret?"
read secret
export UM_SECRET=$secret

echo "bandwidth number?"
read number
export UM_NUMBER=$number
