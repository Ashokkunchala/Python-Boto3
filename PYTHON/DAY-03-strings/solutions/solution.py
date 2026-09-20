service = "aws-ec2-production"
print("Original:", service)
print("Upper:", service.upper())
print("Lower:", service.lower())
print("Length:", len(service))
parts = service.split("-")
print("Service:", parts[1].upper())
print("Environment:", parts[2])
