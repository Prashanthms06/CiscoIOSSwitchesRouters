#This filter plugin will be used to send the HTML code for right and wrong based on the presence and absence of
#key words. This funtion will be used in in reporting. As of 4th Oct 2021, this function is used for generating
#summary of hosts while doing upgradation


class FilterModule(object):

    def generate_table(self,field_name):
        # if the field name is present and the failed is not false
        if field_name=='BasicConfiguration':
            return self.generate_table_basic_info()
        else:
            return ""

    def generate_table_basic_info(self):
        table_information=""
        #start the table tag
        table_information += self.get_table_tag()
        #Start the row tag


        # populate
        for items in pre_upgrade_info.BasicConfiguration.tr:
            table_information += self.get_row_tag()
            table_information += self.get_td_tag()
            table_information += items.td_name
            table_information += self.get_td_tag(end=True)
            table_information += self.get_td_tag()
            table_information += items.td_value
            table_information += self.get_td_tag(end=True)
            table_information += self.get_row_tag(end=True)


        #close the table tag
        table_information += self.get_table_tag(end=True)
        return table_information

    def get_row_tag(self, end=False):
        if end:
          return "<tr>"
        else:
            return "</tr>"

    def get_table_tag(self, end=False):
        if end:
            return "</table>"
        else:
            return "<table>"

    def get_td_tag(self,end=False):
        if end:
            return "</td>"
        else:
            return "<td>"

    def filters(self):
        return {
            'generate_table': self.generate_table,
        }