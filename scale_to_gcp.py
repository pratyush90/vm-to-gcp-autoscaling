from googleapiclient import discovery
import time

# 🔹 Configuration
PROJECT = "tangential-map-491608-v0"   # your project ID
ZONE = "us-central1-a"
GROUP = "flask-group"

def scale_instance_group(new_size):
    try:
        print(f"Scaling MIG to {new_size} instances...")

        # Build Compute Engine client
        service = discovery.build('compute', 'v1')

        # Resize request
        request = service.instanceGroupManagers().resize(
            project=PROJECT,
            zone=ZONE,
            instanceGroupManager=GROUP,
            size=new_size
        )

        response = request.execute()

        print("✅ Scaling request sent successfully!")
        print("Response:", response)

    except Exception as e:
        print("❌ Error during scaling:", str(e))


if __name__ == "__main__":
    # 🔹 Target size (increase from 1 → 2)
    TARGET_SIZE = 2

    scale_instance_group(TARGET_SIZE)