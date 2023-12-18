#include <stdio.h>
#include <Python.h>

/**
 *print_python_bytes - Prints bytes information
 *
 *@p: Python Object
 *Return: no return
 */
void print_python_bytes(PyObject *obj)
{
	char *string;
	long int size, i, limit;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(obj))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject*)(obj))->ob_size;
	string = ((PyBytesObject*) obj)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 *print_python_float - Prints float information
 *
 *@p: Python Object
 *Return: no return
 */
void print_python_float(PyObject *obj)
{
	double value;
	char *formatted_value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(obj))
	{
		printf(" [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject*)(obj))->ob_fval;
	formatted_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", formatted_value);
	setbuf(stdout, NULL);
}

/**
 *print_python_list - Prints list information
 *
 *@p: Python Object
 *Return: no return
 */
void print_python_list(PyObject *obj)
{
	long int size, i;
	PyListObject * list;
	PyObject * item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(obj))
	{
		printf(" [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject*)(obj))->ob_size;
	list = (PyListObject*) obj;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		if (PyFloat_Check(item))
			print_python_float(item);
	}

	setbuf(stdout, NULL);
}
