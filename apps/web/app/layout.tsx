import type { ReactNode } from "react";
import "./globals.css";

export const metadata = {
  title: "TradeBot7x",
  description: "Risk-controlled algorithmic trading platform",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
