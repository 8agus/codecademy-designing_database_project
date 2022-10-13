CREATE TABLE "customer" (
  "cu_id" integer PRIMARY KEY NOT NULL,
  "name" text,
  "last_name" text
);

CREATE TABLE "address" (
  "add_id" integer UNIQUE PRIMARY KEY NOT NULL,
  "str_numb" text,
  "str_name" text,
  "city" text
);

CREATE TABLE "credit_card" (
  "cc_id" integer UNIQUE PRIMARY KEY NOT NULL,
  "card_number" integer,
  "exp_date" integer,
  "cvv_number" integer
);

CREATE TABLE "purchase_history" (
  "ord_id" integer UNIQUE PRIMARY KEY NOT NULL,
  "item_id" integer,
  "quantity" integer,
  "order_date" datetime
);

CREATE TABLE "items" (
  "item_id" integer PRIMARY KEY NOT NULL,
  "item_name" text,
  "item_description" text,
  "price" money
);

ALTER TABLE "address" ADD FOREIGN KEY ("add_id") REFERENCES "customer" ("cu_id");

ALTER TABLE "credit_card" ADD FOREIGN KEY ("cc_id") REFERENCES "customer" ("cu_id");

ALTER TABLE "purchase_history" ADD FOREIGN KEY ("ord_id") REFERENCES "customer" ("cu_id");

ALTER TABLE "purchase_history" ADD FOREIGN KEY ("item_id") REFERENCES "items" ("item_id");
