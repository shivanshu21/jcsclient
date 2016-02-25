from client import common
from client import config

import pprint

# TODO(rushiagr): also check the 'type' of parameter supplied. E.g. don't
# accept 'blah' as a value for InstanceCount, which expects an integer

# =============== Instances =================

def describe_instances():
    """DescribeInstances API wrapper."""
    valid_optional_params = []
    optional_params = {}
    request_dict = {'Action': 'DescribeInstances'}
    return common.do_compute_request(valid_optional_params, optional_params, request_dict)

def run_instances(ImageId, InstanceTypeId, **optional_params):
    """
    Run one or more instances.

    Supported params:
        image_id, instance_type_id, key_name, instance_count, subnet_id,
        private_ip_address
    Unsupported params:
        block_device_mapping, security_group_id. Blocked on '.N' feature
        ambiguity.
    """
    # TODO(rushiagr): support for BlockDeviceMapping.N, SecurityGroupId.N
    valid_optional_params = ['KeyName', 'InstanceCount', 'SubnetId', 'PrivateIPAddress']

    mandatory_params = {
        'Action': 'RunInstances',
        'ImageId': ImageId,
        'InstanceTypeId': InstanceTypeId,
    }

    return common.do_compute_request(valid_optional_params, optional_params, mandatory_params)


def delete_instance():
    pass

def stop_instances():
    """StopInstances API wrapper"""
    pass

def start_instances():
    """StartInstances API wrapper."""
    pass

def reboot_instances():
    """RebootInstances API wrapper."""
    pass

def terminate_instances():
    """TerminateInstances API wrapper."""
    pass

# =============== Images =================

def describe_images():
    """DescribeImages API wrapper."""
    valid_optional_params = []
    optional_params = {}
    request_dict = {'Action': 'DescribeImages'}
    return common.do_compute_request(valid_optional_params, optional_params, request_dict)

# =============== Key pairs =================

def create_key_pair():
    """CreateKeyPair."""
    pass

def delete_key_pair():
    """DelateKeyPair."""
    pass

def import_key_pair():
    """ImportKeyPair."""
    pass

def describe_key_pairs():
    """DescribeKeyPairs."""
    pass

# =============== Volumes =================

def describe_volumes():
    """DescribeVolumes API wrapper."""
    valid_optional_params = []
    mandatory_params = {'Action': 'DescribeVolumes'}
    return common.do_compute_request(valid_optional_params, {}, mandatory_params)

def create_volume(**optional_params):
    """
    CreateVolume API wrapper.

    Either Size or SnapshotId is mandatory.
    """
    if not optional_params.get('Size') and not optional_params.get('SnapshotId'):
        print 'size or snap id is required'
        raise Exception
    valid_optional_params = ['Size', 'SnapshotId']
    mandatory_params = {'Action': 'CreateVolume'}
    return common.do_compute_request(valid_optional_params, optional_params, mandatory_params)

def attach_volume():
    """AttachVolume."""
    pass

def delete_volume(VolumeId):
    valid_optional_params = []
    optional_params = {}
    mandatory_params = {
        'Action': 'DeleteVolume',
        'VolumeId': VolumeId,
    }
    return common.do_compute_request(valid_optional_params, optional_params, mandatory_params)

# =============== Snapshots =================

def describe_snapshots():
    """DescribeSnapshots API wrapper."""
    valid_optional_params = []
    optional_params = {}
    mandatory_params = {'Action': 'DescribeSnapshots'}
    return common.do_compute_request(valid_optional_params, optional_params, mandatory_params)

def create_snapshot(VolumeId, **optional_params):
    """DescribeSnapshots API wrapper."""
    valid_optional_params = ['Name', 'Description']
    mandatory_params = {
        'Action': 'CreateSnapshot',
        'VolumeId': VolumeId,
    }
    return common.do_compute_request(valid_optional_params, optional_params, mandatory_params)

def delete_snapshot(SnapshotId):
    """DescribeSnapshots API wrapper."""
    valid_optional_params = []
    optional_params = {}
    mandatory_params = {
        'Action': 'DeleteSnapshot',
        'SnapshotId': SnapshotId,
    }
    return common.do_compute_request(valid_optional_params, optional_params, mandatory_params)

def describe_vpcs():
    """DescribeVpcs API wrapper."""
    valid_optional_params = []
    optional_params = {}
    request_dict = {'Action': 'DescribeVpcs'}
    return common.do_vpc_request(valid_optional_params, optional_params, request_dict)


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(describe_instances())
    pp.pprint(describe_volumes())
    pp.pprint(describe_images())
    pp.pprint(describe_vpcs())
    #pp.pprint(describe_snapshots())
    #pp.pprint(delete_volume('9e501705-6721-4880-abcd-cd4d8bdbf005'))
    #print create_volume(Size=2)