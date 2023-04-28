class InfluxPoint:
    
    @classmethod
    def __to_point(cls, data, tag_name, point_location):
        point_data = []
        point_data.append("{measurement},location={location} rate={rate},apr={apr}".format(
            measurement = tag_name,
            location = point_location,
            rate = data['rate'],
            apr = data['apr']
            ))
        return point_data

    @classmethod
    def to_point(cls, data, tag_name, point_location):
       influx_point = cls.__to_point(data, tag_name, point_location)
    #    print(f'POINT ({tag_name}): {influx_point}')
       return influx_point  
