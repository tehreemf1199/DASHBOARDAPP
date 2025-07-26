{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ef2fb468-e4eb-4cde-b63e-e494a22afdb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from dash import html,dcc,Input,Output,State,dash_table \n",
    "import plotly.express as px\n",
    "import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eb68481e-965a-4101-a960-2d1f47c0c6fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Account</th>\n",
       "      <th>Description</th>\n",
       "      <th>Debit</th>\n",
       "      <th>Credit</th>\n",
       "      <th>Category</th>\n",
       "      <th>Transaction_Type</th>\n",
       "      <th>Customer_Vendor</th>\n",
       "      <th>Payment_Method</th>\n",
       "      <th>Reference</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2023-08-21</td>\n",
       "      <td>Accounts Payable</td>\n",
       "      <td>Transaction 1</td>\n",
       "      <td>112.56</td>\n",
       "      <td>112.56</td>\n",
       "      <td>Asset</td>\n",
       "      <td>Sale</td>\n",
       "      <td>Customer 39</td>\n",
       "      <td>Cash</td>\n",
       "      <td>67471</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2023-08-13</td>\n",
       "      <td>Accounts Receivable</td>\n",
       "      <td>Transaction 2</td>\n",
       "      <td>775.86</td>\n",
       "      <td>775.86</td>\n",
       "      <td>Revenue</td>\n",
       "      <td>Purchase</td>\n",
       "      <td>Customer 3</td>\n",
       "      <td>Check</td>\n",
       "      <td>92688</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2023-05-11</td>\n",
       "      <td>Accounts Receivable</td>\n",
       "      <td>Transaction 3</td>\n",
       "      <td>332.81</td>\n",
       "      <td>332.81</td>\n",
       "      <td>Revenue</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Customer 36</td>\n",
       "      <td>Check</td>\n",
       "      <td>72066</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2023-02-26</td>\n",
       "      <td>Accounts Receivable</td>\n",
       "      <td>Transaction 4</td>\n",
       "      <td>203.71</td>\n",
       "      <td>203.71</td>\n",
       "      <td>Asset</td>\n",
       "      <td>Purchase</td>\n",
       "      <td>Customer 57</td>\n",
       "      <td>Check</td>\n",
       "      <td>27973</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2023-11-06</td>\n",
       "      <td>Accounts Receivable</td>\n",
       "      <td>Transaction 5</td>\n",
       "      <td>986.26</td>\n",
       "      <td>986.26</td>\n",
       "      <td>Asset</td>\n",
       "      <td>Expense</td>\n",
       "      <td>Customer 92</td>\n",
       "      <td>Check</td>\n",
       "      <td>29758</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99995</th>\n",
       "      <td>2023-06-13</td>\n",
       "      <td>Inventory</td>\n",
       "      <td>Transaction 99996</td>\n",
       "      <td>585.75</td>\n",
       "      <td>585.75</td>\n",
       "      <td>Liability</td>\n",
       "      <td>Expense</td>\n",
       "      <td>Customer 66</td>\n",
       "      <td>Check</td>\n",
       "      <td>13348</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99996</th>\n",
       "      <td>2023-09-14</td>\n",
       "      <td>Accounts Payable</td>\n",
       "      <td>Transaction 99997</td>\n",
       "      <td>785.01</td>\n",
       "      <td>785.01</td>\n",
       "      <td>Liability</td>\n",
       "      <td>Sale</td>\n",
       "      <td>Customer 77</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>43646</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99997</th>\n",
       "      <td>2023-02-08</td>\n",
       "      <td>Cash</td>\n",
       "      <td>Transaction 99998</td>\n",
       "      <td>502.68</td>\n",
       "      <td>502.68</td>\n",
       "      <td>Revenue</td>\n",
       "      <td>Expense</td>\n",
       "      <td>Customer 17</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>39071</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99998</th>\n",
       "      <td>2023-07-05</td>\n",
       "      <td>Inventory</td>\n",
       "      <td>Transaction 99999</td>\n",
       "      <td>789.19</td>\n",
       "      <td>789.19</td>\n",
       "      <td>Asset</td>\n",
       "      <td>Purchase</td>\n",
       "      <td>Customer 100</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>69225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99999</th>\n",
       "      <td>2023-07-23</td>\n",
       "      <td>Accounts Receivable</td>\n",
       "      <td>Transaction 100000</td>\n",
       "      <td>484.13</td>\n",
       "      <td>484.13</td>\n",
       "      <td>Asset</td>\n",
       "      <td>Expense</td>\n",
       "      <td>Customer 62</td>\n",
       "      <td>Bank Transfer</td>\n",
       "      <td>88567</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100000 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Date              Account         Description   Debit  Credit  \\\n",
       "0      2023-08-21     Accounts Payable       Transaction 1  112.56  112.56   \n",
       "1      2023-08-13  Accounts Receivable       Transaction 2  775.86  775.86   \n",
       "2      2023-05-11  Accounts Receivable       Transaction 3  332.81  332.81   \n",
       "3      2023-02-26  Accounts Receivable       Transaction 4  203.71  203.71   \n",
       "4      2023-11-06  Accounts Receivable       Transaction 5  986.26  986.26   \n",
       "...           ...                  ...                 ...     ...     ...   \n",
       "99995  2023-06-13            Inventory   Transaction 99996  585.75  585.75   \n",
       "99996  2023-09-14     Accounts Payable   Transaction 99997  785.01  785.01   \n",
       "99997  2023-02-08                 Cash   Transaction 99998  502.68  502.68   \n",
       "99998  2023-07-05            Inventory   Transaction 99999  789.19  789.19   \n",
       "99999  2023-07-23  Accounts Receivable  Transaction 100000  484.13  484.13   \n",
       "\n",
       "        Category Transaction_Type Customer_Vendor Payment_Method  Reference  \n",
       "0          Asset             Sale     Customer 39           Cash      67471  \n",
       "1        Revenue         Purchase      Customer 3          Check      92688  \n",
       "2        Revenue         Transfer     Customer 36          Check      72066  \n",
       "3          Asset         Purchase     Customer 57          Check      27973  \n",
       "4          Asset          Expense     Customer 92          Check      29758  \n",
       "...          ...              ...             ...            ...        ...  \n",
       "99995  Liability          Expense     Customer 66          Check      13348  \n",
       "99996  Liability             Sale     Customer 77    Credit Card      43646  \n",
       "99997    Revenue          Expense     Customer 17    Credit Card      39071  \n",
       "99998      Asset         Purchase    Customer 100    Credit Card      69225  \n",
       "99999      Asset          Expense     Customer 62  Bank Transfer      88567  \n",
       "\n",
       "[100000 rows x 10 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(\"E:/financial_accounting.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d6a6e8d5-d623-4e49-9c17-6b4bb565b3d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date                0\n",
       "Account             0\n",
       "Description         0\n",
       "Debit               0\n",
       "Credit              0\n",
       "Category            0\n",
       "Transaction_Type    0\n",
       "Customer_Vendor     0\n",
       "Payment_Method      0\n",
       "Reference           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e0465422-23c4-4cd8-bf4a-ec9e610a114f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 100000 entries, 0 to 99999\n",
      "Data columns (total 10 columns):\n",
      " #   Column            Non-Null Count   Dtype  \n",
      "---  ------            --------------   -----  \n",
      " 0   Date              100000 non-null  object \n",
      " 1   Account           100000 non-null  object \n",
      " 2   Description       100000 non-null  object \n",
      " 3   Debit             100000 non-null  float64\n",
      " 4   Credit            100000 non-null  float64\n",
      " 5   Category          100000 non-null  object \n",
      " 6   Transaction_Type  100000 non-null  object \n",
      " 7   Customer_Vendor   100000 non-null  object \n",
      " 8   Payment_Method    100000 non-null  object \n",
      " 9   Reference         100000 non-null  int64  \n",
      "dtypes: float64(2), int64(1), object(7)\n",
      "memory usage: 7.6+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "edbec2d9-142b-43f7-bb38-82866f747431",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Debit</th>\n",
       "      <th>Credit</th>\n",
       "      <th>Reference</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>607.747368</td>\n",
       "      <td>607.747368</td>\n",
       "      <td>54859.916200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>254.906370</td>\n",
       "      <td>254.906370</td>\n",
       "      <td>25956.740346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>3.880000</td>\n",
       "      <td>3.880000</td>\n",
       "      <td>10000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>401.637500</td>\n",
       "      <td>401.637500</td>\n",
       "      <td>32367.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>634.080000</td>\n",
       "      <td>634.080000</td>\n",
       "      <td>54810.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>829.990000</td>\n",
       "      <td>829.990000</td>\n",
       "      <td>77302.250000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>999.990000</td>\n",
       "      <td>999.990000</td>\n",
       "      <td>99999.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Debit         Credit      Reference\n",
       "count  100000.000000  100000.000000  100000.000000\n",
       "mean      607.747368     607.747368   54859.916200\n",
       "std       254.906370     254.906370   25956.740346\n",
       "min         3.880000       3.880000   10000.000000\n",
       "25%       401.637500     401.637500   32367.000000\n",
       "50%       634.080000     634.080000   54810.500000\n",
       "75%       829.990000     829.990000   77302.250000\n",
       "max       999.990000     999.990000   99999.000000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b6cf5544-d6d3-4a7a-9c05-2370fcc853dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0202b128-6379-43f0-a6b3-13ab893b310c",
   "metadata": {},
   "source": [
    "we can see that data is clean contain not any null value and no duplication found . The data describes that there is not outlier so data is fine we can move forward"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0bd51d33-60a8-4974-9f75-2c0fa23e075a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Account\n",
       "Accounts Payable       25104\n",
       "Inventory              25054\n",
       "Accounts Receivable    25038\n",
       "Cash                   24804\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Account.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a26baa85-6a49-454c-b9f8-67481a402723",
   "metadata": {},
   "outputs": [],
   "source": [
    "receivables = df[df[\"Account\"] == \"Accounts Receivable\"]\n",
    "payables = df[df[\"Account\"] == \"Accounts Payable\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1b579843-1170-4931-a51f-8074099168e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "total_receivable = receivables[\"Credit\"].sum()\n",
    "total_payable = payables[\"Credit\"].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "140d8a4d-37d0-4ede-baf1-2c0d25893adb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15272312.940000001 15152628.73\n"
     ]
    }
   ],
   "source": [
    "print(total_receivable ,total_payable)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e619b1a4-f82a-4e82-9f01-1e84e61d4007",
   "metadata": {},
   "source": [
    "KPI\tAmount (USD)\n",
    "Receivables\t💵 15.27 million\n",
    "Payables\t💸 15.15 million\n",
    "\n",
    "This shows:\n",
    "\n",
    "your business is owed slightly more than it owes.\n",
    "\n",
    "You have a positive receivables balance overall."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "28dae01a-53b1-4277-abe9-f59c29f31616",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Debit</th>\n",
       "      <th>Credit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Asset</td>\n",
       "      <td>15270030.86</td>\n",
       "      <td>15270030.86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Expense</td>\n",
       "      <td>15163910.14</td>\n",
       "      <td>15163910.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Liability</td>\n",
       "      <td>15072434.67</td>\n",
       "      <td>15072434.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Revenue</td>\n",
       "      <td>15268361.16</td>\n",
       "      <td>15268361.16</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Category        Debit       Credit\n",
       "0      Asset  15270030.86  15270030.86\n",
       "1    Expense  15163910.14  15163910.14\n",
       "2  Liability  15072434.67  15072434.67\n",
       "3    Revenue  15268361.16  15268361.16"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary1=df.groupby(\"Category\")[[\"Debit\",\"Credit\"]].agg(\"sum\").reset_index()\n",
    "summary1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c255522b-23fc-40e4-af4f-f853f7aea601",
   "metadata": {},
   "source": [
    " Insight:\n",
    "\n",
    "Your expenses and revenues are close, suggesting a balanced cash cycle.\n",
    "\n",
    "Total assets slightly outweigh liabilities—shows moderate financial health."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "df82ade9-0655-46bc-b8a7-d3f83ed005aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Payment_Method</th>\n",
       "      <th>Debit</th>\n",
       "      <th>Credit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bank Transfer</td>\n",
       "      <td>15176092.28</td>\n",
       "      <td>15176092.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cash</td>\n",
       "      <td>15147309.99</td>\n",
       "      <td>15147309.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Check</td>\n",
       "      <td>15324618.14</td>\n",
       "      <td>15324618.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Credit Card</td>\n",
       "      <td>15126716.42</td>\n",
       "      <td>15126716.42</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Payment_Method        Debit       Credit\n",
       "0  Bank Transfer  15176092.28  15176092.28\n",
       "1           Cash  15147309.99  15147309.99\n",
       "2          Check  15324618.14  15324618.14\n",
       "3    Credit Card  15126716.42  15126716.42"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary2=df.groupby(\"Payment_Method\")[[\"Debit\",\"Credit\"]].agg(\"sum\").reset_index()\n",
    "summary2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc9aff36-7df8-4b8a-a456-9066da540e37",
   "metadata": {},
   "source": [
    "Most payments are made by Check—this can help optimize payment processing strategies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "26f4d603-cde4-46d7-8bd3-970a9fae320b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x19498652710>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# financial_dashboard.py\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "from dash import Dash, html, dcc\n",
    "import os\n",
    "\n",
    "# Load or create data\n",
    "file_path = os.path.expanduser(\"~/Desktop/financial_Accounting.csv\")\n",
    "if not os.path.exists(file_path):\n",
    "    data = {\n",
    "        \"Date\": pd.date_range(start=\"2024-01-01\", periods=100, freq=\"D\"),\n",
    "        \"Category\": [\"Groceries\", \"Utilities\", \"Rent\", \"Transport\", \"Entertainment\"] * 20,\n",
    "        \"Credit\": [500, 0, 0, 0, 0] * 20,\n",
    "        \"Debit\": [0, 150, 1000, 100, 200] * 20,\n",
    "        \"Payment_Method\": [\"Cash\", \"Bank\", \"Card\", \"Online\", \"Check\"] * 20\n",
    "    }\n",
    "    pd.DataFrame(data).to_csv(file_path, index=False)\n",
    "\n",
    "df = pd.read_csv(file_path)\n",
    "df[\"Date\"] = pd.to_datetime(df[\"Date\"])\n",
    "\n",
    "# KPIs\n",
    "total_credit = df[\"Credit\"].sum()\n",
    "total_debit = df[\"Debit\"].sum()\n",
    "net_balance = total_credit - total_debit\n",
    "\n",
    "# Create Dash app\n",
    "app = Dash(__name__)\n",
    "app.title = \"💰 Financial Dashboard\"\n",
    "\n",
    "app.layout = html.Div(style={\n",
    "    \"backgroundColor\": \"#000\",\n",
    "    \"color\": \"#FFD700\",\n",
    "    \"fontFamily\": \"Arial\",\n",
    "    \"padding\": \"20px\"\n",
    "}, children=[\n",
    "    html.H1(\"📊 Financial Dashboard\", style={\"textAlign\": \"center\"}),\n",
    "\n",
    "    html.Div([\n",
    "        html.Div([\n",
    "            html.H4(\"Total Credit\"),\n",
    "            html.H2(f\"${total_credit:,.2f}\")\n",
    "        ], style={\"backgroundColor\": \"#222\", \"padding\": \"15px\", \"borderRadius\": \"10px\", \"width\": \"30%\"}),\n",
    "\n",
    "        html.Div([\n",
    "            html.H4(\"Total Debit\"),\n",
    "            html.H2(f\"${total_debit:,.2f}\")\n",
    "        ], style={\"backgroundColor\": \"#222\", \"padding\": \"15px\", \"borderRadius\": \"10px\", \"width\": \"30%\"}),\n",
    "\n",
    "        html.Div([\n",
    "            html.H4(\"Net Balance\"),\n",
    "            html.H2(f\"${net_balance:,.2f}\")\n",
    "        ], style={\"backgroundColor\": \"#222\", \"padding\": \"15px\", \"borderRadius\": \"10px\", \"width\": \"30%\"})\n",
    "    ], style={\"display\": \"flex\", \"justifyContent\": \"space-around\", \"marginBottom\": \"30px\"}),\n",
    "\n",
    "    dcc.Graph(figure=px.bar(df, x=\"Category\", y=\"Debit\", color=\"Category\",\n",
    "                            title=\"Debit by Category\", template=\"plotly_dark\",\n",
    "                            color_discrete_sequence=[\"#FFD700\"])),\n",
    "    \n",
    "    dcc.Graph(figure=px.line(df.groupby(\"Date\")[\"Credit\"].sum().reset_index(),\n",
    "                             x=\"Date\", y=\"Credit\", title=\"Credit Over Time\",\n",
    "                             template=\"plotly_dark\", markers=True, line_shape=\"spline\",\n",
    "                             color_discrete_sequence=[\"#FFD700\"])),\n",
    "\n",
    "    dcc.Graph(figure=px.pie(df, names=\"Payment_Method\", values=\"Debit\",\n",
    "                            title=\"Payment Methods Share\", template=\"plotly_dark\",\n",
    "                            color_discrete_sequence=px.colors.sequential.YlOrBr)),\n",
    "\n",
    "    dcc.Graph(figure=px.density_heatmap(df, x=\"Category\", y=\"Payment_Method\", z=\"Debit\",\n",
    "                                        title=\"Heatmap of Debit by Category and Payment Method\",\n",
    "                                        template=\"plotly_dark\", color_continuous_scale=\"YlOrBr\")),\n",
    "])\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c6d7590-9c8b-4c9f-a259-90ac1a272821",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "202976ac-d33a-4c9a-8de5-ef7e3305fbf3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e242b4a7-56d4-4145-b408-27db6c5d0d80",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
