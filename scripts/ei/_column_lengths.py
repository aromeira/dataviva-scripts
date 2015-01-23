import pandas as pd
def add_column_length(table_name, table_data):
	columns = {'b': 'bra_id', 'c': 'course_hedu_id'}
	for index, column in columns.items():
		if index in table_name:
			table_data[column + "_len"] = pd.Series( map(lambda x: len(str(x)), table_data.index.get_level_values(column)), index = table_data.index)

	return table_data