import boto3

class StorageService(object):
    def __init__(self):
        self.s3 = boto3.client('s3')

    def get_area(self, region, area):
        try:
            s3Object = self.s3.get_object(Bucket="sa.area", Key=region+"."+area+".map")
            area = s3Object['Body'].read().strip(' \t\n\r').split('\n')
            for i in range(len(area)):
                area[i] = list(area[i])
            return area
        except Exception as e:
            print e
            return
